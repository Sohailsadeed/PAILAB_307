# 📧 Email Reply Generator - Full Stack System

An intelligent email reply generation system built with Spring Boot (Backend), a Web Frontend, and a Browser Extension.

This project follows a clean layered backend architecture with database integration and AOP-based logging, and is supported by a separate frontend application and browser extension for real-world usability.

---

# 🏗️ System Architecture

```
User
  │
  ├── 🌐 Web Frontend (email-reply-generator-frontend)
  │
  ├── 🧩 Browser Extension (email-reply-generator-extension)
  │
  ▼
Spring Boot Backend API (email-reply-generator-backend)
  │
  ▼
Database
```

---

# 🚀 Repositories

### 🖥 Backend API
Repository: `email-reply-generator-backend`

- Spring Boot
- REST APIs
- Database Integration (JPA / Hibernate)
- Logging with AOP
- Layered Architecture

---

### 🌐 Frontend Application
Repository: `email-reply-generator-frontend`

- Connects to backend REST APIs
- Sends email content
- Displays generated replies
- Clean UI for user interaction

---

### 🧩 Browser Extension
Repository: `email-reply-generator-extension`

- Integrates directly into browser
- Enhances email workflow
- Sends displayed email content to backend
- Displays AI-generated reply instantly

---

# 🛠️ Backend Tech Stack

- Java 17+
- Spring Boot
- Spring Web
- Spring Data JPA
- Hibernate
- Spring AOP
- Maven
- MySQL

---

# 📁 Backend Project Structure

```
src/main/java/com/email/writer/
│
├── aop/                # Logging aspects
├── config/             # Configuration classes
├── controllers/        # REST controllers
├── dao/                # Data access layer
├── dtos/               # Data Transfer Objects
├── services/           # Business logic
└── EmailGeneratorApplication.java
```

---

# 🧠 Architecture Design

Controller → Service → DAO → Database

- Controllers handle HTTP requests
- Services implement business logic
- DAO layer communicates with database
- DTOs structure request/response payloads
- AOP handles centralized logging

---

# 🗄️ Database Configuration

Update `application.properties`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/your_database
spring.datasource.username=your_username
spring.datasource.password=your_password

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

---

# ▶️ Running the Backend

```bash
git clone https://github.com/Sohailsadeed/email-reply-generator-backend.git
cd email-reply-generator-backend
./mvnw spring-boot:run
```

Server runs at:

```
http://localhost:8080
```

---

# 🔌 Example API Endpoint

```
POST /api/email/generate
```

Request:

```json
{
  "emailContent": "Write a professional reply accepting the meeting."
  "tone":"Preferred tone(i.e Professional/ Casual/ Friendly/ Sarcastic)"
}
```

Response:

```json
{
  "generatedReply": "Thank you for your invitation. I would be happy to attend..."
}
```

---

# 🔮 Future Improvements

- JWT Authentication
- Deployment to AWS / Render
- Advanced prompt customization
- Usage analytics

---
