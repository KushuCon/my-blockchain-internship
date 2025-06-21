    use actix_web::{web, App, HttpServer, Responder, HttpResponse};
    use serde::{Deserialize, Serialize};
    use std::collections::HashMap;
    use std::sync::Arc;
    use parking_lot::Mutex;
    use actix_cors::Cors;
    use actix_files as fs; 

    #[derive(Debug, Clone, Serialize, Deserialize)]
    struct Task {
        id: u32,
        description: String,
        completed: bool,
    }

    impl Task {
        fn new(id: u32, description: String) -> Self {
            Task { id, description, completed: false }
        }
    }

    #[derive(Debug, Serialize, Deserialize)]
    struct NewTask {
        description: String,
    }

    #[derive(Debug, Serialize, Deserialize)]
    struct UpdateTask {
        description: Option<String>,
        completed: Option<bool>,
    }

    struct AppState {
        tasks: Mutex<HashMap<u32, Task>>,
        next_id: Mutex<u32>,
    }

    async fn get_tasks(data: web::Data<AppState>) -> impl Responder {
        let tasks = data.tasks.lock();
        HttpResponse::Ok().json(tasks.values().cloned().collect::<Vec<Task>>())
    }

    async fn get_task_by_id(data: web::Data<AppState>, path: web::Path<u32>) -> impl Responder {
        let id = path.into_inner();
        let tasks = data.tasks.lock();
        if let Some(task) = tasks.get(&id) {
            HttpResponse::Ok().json(task)
        } else {
            HttpResponse::NotFound().body(format!("Task with ID {} not found", id))
        }
    }

    async fn create_task(data: web::Data<AppState>, new_task: web::Json<NewTask>) -> impl Responder {
        let mut tasks = data.tasks.lock();
        let mut next_id = data.next_id.lock();

        let id = *next_id;
        let task = Task::new(id, new_task.description.clone());

        tasks.insert(id, task.clone());
        *next_id += 1;

        HttpResponse::Created().json(task)
    }

    async fn update_task(
        data: web::Data<AppState>,
        path: web::Path<u32>,
        updated_fields: web::Json<UpdateTask>,
    ) -> impl Responder {
        let id = path.into_inner();
        let mut tasks = data.tasks.lock();

        if let Some(task) = tasks.get_mut(&id) {
            if let Some(description) = &updated_fields.description {
                task.description = description.clone();
            }
            if let Some(completed) = updated_fields.completed {
                task.completed = completed;
            }
            HttpResponse::Ok().json(task.clone())
        } else {
            HttpResponse::NotFound().body(format!("Task with ID {} not found", id))
        }
    }

    async fn delete_task(data: web::Data<AppState>, path: web::Path<u32>) -> impl Responder {
        let id = path.into_inner();
        let mut tasks = data.tasks.lock();

        if tasks.remove(&id).is_some() {
            HttpResponse::NoContent().finish()
        } else {
            HttpResponse::NotFound().body(format!("Task with ID {} not found", id))
        }
    }

    #[actix_web::main]
    async fn main() -> std::io::Result<()> {
        let app_state = Arc::new(AppState {
            tasks: Mutex::new(HashMap::new()),
            next_id: Mutex::new(1),
        });

        println!("Starting Rust server at http://127.0.0.1:8080");

        HttpServer::new(move || {
            App::new()
                .wrap(
                    Cors::permissive()
                        .allow_any_origin()
                        .allow_any_method()
                        .allow_any_header()
                        .max_age(3600),
                )
                .app_data(web::Data::from(app_state.clone()))
                .service(
                    web::scope("/api/tasks") 
                        .route("", web::get().to(get_tasks))
                        .route("", web::post().to(create_task))
                        .route("/{id}", web::get().to(get_task_by_id))
                        .route("/{id}", web::put().to(update_task))
                        .route("/{id}", web::delete().to(delete_task)),
                )
                .service(fs::Files::new("/", "./static").index_file("index.html"))
        })
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
    }
    
