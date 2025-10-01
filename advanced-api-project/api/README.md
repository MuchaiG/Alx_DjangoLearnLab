# 📘 API Views Documentation

This document provides a detailed explanation of how each Django REST Framework (DRF) view is configured and intended to operate in the `advanced_api_project`. The project implements a simple `Book` API with full CRUD functionality, custom validation, filtering, and permission handling.

---

## Overview

The API exposes endpoints for managing `Book` resources. It includes the following operations:

- List all books  
- Retrieve a single book  
- Create a new book  
- Update an existing book  
- Delete a book  

Each view uses **DRF generic class-based views**, which provide built-in functionality for common operations, and has been customized for validation, permissions, and query handling.

---

## Views Overview

| View Class         | URL Pattern                      | HTTP Methods        | Description                                     | Permissions                      |
|--------------------|----------------------------------|---------------------|--------------------------------------------------|----------------------------------|
| `BookListView`     | `/api/books/`                   | `GET`               | Retrieve all books in the database.              | Public (no authentication)      |
| `BookDetailView`   | `/api/books/<int:pk>/`          | `GET`               | Retrieve details of a specific book by ID.       | Public (no authentication)      |
| `BookCreateView`   | `/api/books/create/`            | `POST`              | Add a new book to the database.                  | Authenticated users only        |
| `BookUpdateView`   | `/api/books/<int:pk>/update/`   | `PUT`, `PATCH`      | Modify an existing book.                         | Authenticated users only        |
| `BookDeleteView`   | `/api/books/<int:pk>/delete/`   | `DELETE`            | Remove a book from the database.                 | Authenticated users only        |

---

## 1. BookListView

File: `api/views.py`  
Class: `BookListView`  
Base: `generics.ListAPIView`

## 2. BookDetailView

File: `api/views.py`
Class: `BookDetailView`
Base: `generics.RetrieveAPIView`

## 3. BookCreateView

File: `api/views.py`
Class: `BookCreateView`
Base: `generics.CreateAPIView`

## 4. BookUpdateView

File: `api/views.py`
Class: `BookUpdateView`
Base: `enerics.UpdateAPIView`

## 5. BookDeleteView

File: `api/views.py`
Class: `BookDeleteView`
Base: `generics.DestroyAPIView`

## Permissions Summary
| View             | Permission Class  | Access Level             |
| ---------------- | ----------------- | ------------------------ |
| `BookListView`   | `AllowAny`        | Public                   |
| `BookDetailView` | `AllowAny`        | Public                   |
| `BookCreateView` | `IsAuthenticated` | Authenticated users only |
| `BookUpdateView` | `IsAuthenticated` | Authenticated users only |
| `BookDeleteView` | `IsAuthenticated` | Authenticated users only |
