---

Title: "Structure of Project"

Status:

marker:

tags:

Date: "2026.08.01"

Time: "17:42"

---
# Structure of Project

# Separation Between the RAG Engine and Study Application

The project should be divided into two independent systems:

```text
Reusable RAG Engine
        │
        ▼
Study Application
```

The RAG engine should contain only generic retrieval and generation capabilities. It should know nothing about colleges, semesters, subjects, students, exams, or study plans.

The study application should contain all education-specific behavior and use the RAG engine as a dependency.

## Proposed Repository Structure

```text
rag-notes-platform/
│
├── packages/
│   │
│   └── rag_engine/
│       # Reusable RAG library that can later be used by
│       # other products such as legal search, company
│       # knowledge bases, compliance tools, or documentation assistants.
│       │
│       ├── pyproject.toml
│       ├── README.md
│       │
│       ├── src/
│       │   └── rag_engine/
│       │       ├── __init__.py
│       │       ├── config.py
│       │       ├── bootstrap.py
│       │       │
│       │       ├── domain/
│       │       │   ├── models.py
│       │       │   └── exceptions.py
│       │       │
│       │       ├── services/
│       │       │   ├── indexing_service.py
│       │       │   ├── retrieval_service.py
│       │       │   ├── reranking_service.py
│       │       │   └── generation_service.py
│       │       │
│       │       ├── ports/
│       │       │   ├── embedding_provider.py
│       │       │   ├── vector_repository.py
│       │       │   ├── document_repository.py
│       │       │   ├── reranker_provider.py
│       │       │   └── llm_provider.py
│       │       │
│       │       └── infrastructure/
│       │           ├── parsers/
│       │           ├── chunking/
│       │           ├── embeddings/
│       │           ├── vector_stores/
│       │           ├── rerankers/
│       │           ├── llms/
│       │           └── persistence/
│       │
│       └── tests/
│
├── apps/
│   │
│   └── study_app/
│       # Product-specific application for students.
│       # This layer understands colleges, courses,
│       # semesters, subjects, notes, exams, and users.
│       │
│       ├── pyproject.toml
│       ├── README.md
│       │
│       ├── src/
│       │   └── study_app/
│       │       ├── __init__.py
│       │       ├── config.py
│       │       ├── bootstrap.py
│       │       │
│       │       ├── domain/
│       │       │   ├── student.py
│       │       │   ├── college.py
│       │       │   ├── course.py
│       │       │   ├── semester.py
│       │       │   ├── subject.py
│       │       │   ├── note.py
│       │       │   └── study_collection.py
│       │       │
│       │       ├── services/
│       │       │   ├── note_upload_service.py
│       │       │   ├── subject_search_service.py
│       │       │   ├── study_chat_service.py
│       │       │   ├── revision_service.py
│       │       │   └── course_management_service.py
│       │       │
│       │       ├── repositories/
│       │       │   ├── user_repository.py
│       │       │   ├── subject_repository.py
│       │       │   ├── note_repository.py
│       │       │   └── collection_repository.py
│       │       │
│       │       ├── interfaces/
│       │       │   ├── cli/
│       │       │   └── api/
│       │       │
│       │       └── infrastructure/
│       │           ├── database/
│       │           ├── storage/
│       │           └── authentication/
│       │
│       └── tests/
│
├── frontend/
│   # Future web interface for the study application.
│
├── data/
│   ├── notes/
│   ├── indexes/
│   └── databases/
│
├── docker-compose.yml
└── README.md
```

## Responsibility of the RAG Engine

The RAG engine should only understand generic concepts.

| Component              | Responsibility                                  |
| ---------------------- | ----------------------------------------------- |
| [[Document ingestion]] | Accept documents and extract their content.     |
| [[Parsing]]            | Convert supported files into normalized text.   |
| [[Chunking]]           | Split documents into searchable chunks.         |
| [[Embeddings]]         | Generate vectors for chunks and queries.        |
| [[Vector storage]]     | Store and retrieve embeddings.                  |
| [[Retrieval]]          | Find the most relevant chunks for a query.      |
| [[Reranking]]          | Improve the ordering of retrieved results.      |
| [[Generation]]         | Send retrieved context to a local LLM.          |
| [[Citations]]          | Preserve source metadata for generated answers. |
| [[Evaluation]]         | Measure retrieval and answer quality.           |

The engine should work with generic metadata:

```python
{
    "document_id": "doc-123",
    "source": "notes/example.pdf",
    "page": 8,
    "title": "Example Document",
    "tags": ["optional", "generic"]
}
```

It should not require fields such as:

```text
college
semester
subject
faculty
exam
student
```

Those belong to the study application.

## Responsibility of the Study Application

The study application adds product-specific meaning around the generic RAG engine.

| Component            | Responsibility                                                         |
| -------------------- | ---------------------------------------------------------------------- |
| College organization | Group content by institution, department, and programme.               |
| Course structure     | Organize material by course, semester, subject, and unit.              |
| User management      | Handle students, faculty, administrators, and permissions.             |
| Note contribution    | Allow users to upload and manage study material.                       |
| Subject search       | Restrict retrieval to selected subjects or semesters.                  |
| Study chat           | Answer questions using course-specific material.                       |
| Revision tools       | Generate summaries, revision notes, and practice questions.            |
| Quality controls     | Rate, verify, report, and deduplicate uploaded notes.                  |
| Access control       | Define whether notes are private, class-only, college-wide, or public. |

## How the Study Application Uses the RAG Engine

```text
Student asks a question
        │
        ▼
Study Application
        │
        ├── checks user permissions
        ├── identifies college
        ├── identifies semester
        ├── identifies subject
        └── creates metadata filters
        │
        ▼
RAG Engine
        │
        ├── embeds query
        ├── retrieves chunks
        ├── reranks results
        └── generates answer
        │
        ▼
Study Application
        │
        ├── formats citations
        ├── shows subject information
        └── presents the answer
```

Example call:

```python
results = rag_engine.search(
    query="Explain the PLC scan cycle",
    filters={
        "collection_id": "cybersecurity-semester-7",
        "subject_id": "ot-security"
    }
)
```

The RAG engine sees only generic filters.

The study application knows that those identifiers represent a semester and subject.

## Dependency Direction

```text
Study Application
        │
        ▼
    RAG Engine
```

The RAG engine must never import code from the study application.

Correct:

```python
from rag_engine.services import RetrievalService
```

Incorrect:

```python
from study_app.domain import Subject
```

This ensures the RAG engine remains reusable.


  

# References


###### Information
- date: 2026.08.01
- time: 17:42