import React from 'react';


const App = () => {
  return (
    <div className="container">
      {/* Header */}
      <header className="header">
        <div className="logo">BrightWeb</div>
        <nav className="nav">
          <a href="#hero">Home</a>
          <a href="#testimonials">Reviews</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>

      {/* Hero Section */}
      <section id="hero" className="hero">
        <div className="hero-content">
          <h1>Grow Your Business with BrightWeb</h1>
          <p>We help startups and businesses build amazing digital products that users love.</p>
          <button>Learn More</button>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials" className="testimonials">
        <h2>What Clients Say</h2>
        <div className="testimonial-grid">
          <div className="testimonial-card">
            <p>"BrightWeb helped us scale quickly with an intuitive design. Loved working with them!"</p>
            <span>- Emily R.</span>
          </div>
          <div className="testimonial-card">
            <p>"Fantastic service and support. Highly recommended for startups."</p>
            <span>- Michael B.</span>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="contact">
        <h2>Contact Us</h2>
        <form className="contact-form">
          <input type="text" placeholder="Your Name" required />
          <input type="email" placeholder="Your Email" required />
          <textarea rows="4" placeholder="Your Message" required></textarea>
          <button type="submit">Send</button>
        </form>
      </section>

      {/* Footer */}
      <footer className="footer">
        <p>&copy; 2025 BrightWeb. Built with ❤️ for the web.</p>
      </footer>
    </div>
  );
};

export default App;
