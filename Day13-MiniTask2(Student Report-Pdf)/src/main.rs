use printpdf::*;
use std::fs::File;
use std::io::{BufWriter, stdin, Write};
use text_io::read;

fn calculate_average(total: f32, subjects: u32) -> f32 {
    total / subjects as f32
}

fn assign_grade(avg: f32) -> char {
    if avg >= 90.0 {
        'A'
    } else if avg >= 75.0 {
        'B'
    } else if avg >= 60.0 {
        'C'
    } else {
        'D'
    }
}

fn create_pdf(name: &str, total: f32, subjects: u32, average: f32, grade: char) {
    let (doc, page1, layer1) = PdfDocument::new("Report Card", Mm(210.0), Mm(297.0), "Layer 1");
    let layer = doc.get_page(page1).get_layer(layer1);
    let font = doc.add_external_font(File::open("fonts/Poppins-Black.ttf").unwrap()).unwrap();

    let lines = vec![
        "Report Card".to_string(),
        "".to_string(),
        format!("Student Name: {}", name),
        format!("Total Marks: {}", total),
        format!("Subjects: {}", subjects),
        format!("Average: {:.2}", average),
        format!("Grade: {}", grade),
    ];

    let mut y = 270.0;
    for line in lines {
        layer.use_text(line, 12.0, Mm(20.0), Mm(y), &font);
        y -= 10.0;
    }

    doc.save(&mut BufWriter::new(File::create("report_card.pdf").unwrap())).unwrap();
}

fn main() {
    println!("Enter student name:");
    let mut name = String::new();
    stdin().read_line(&mut name).unwrap();
    let name = name.trim();

    println!("Enter total marks:");
    let total: f32 = read!();

    println!("Enter number of subjects:");
    let subjects: u32 = read!();

    let average = calculate_average(total, subjects);
    let grade = assign_grade(average);

    println!("\nGenerating report...");
    create_pdf(name, total, subjects, average, grade);
    println!("Report card generated as 'report_card.pdf'");
}
