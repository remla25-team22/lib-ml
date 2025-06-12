# lib-ml

This repository contains the **preprocessing library** used across multiple components of the REMLA project (Team 22).  
It provides reusable functions for cleaning, transforming, and preparing input text data for sentiment analysis.

---

##  Repository Structure

```
lib-ml/
├── lib_ml/                 # Python module with preprocessing logic
├── requirements.txt        # Runtime dependencies
├── setup.py                # Packaging config
├── VERSION.txt             # Semantic version (e.g., v1.0.0)
└── .github/workflows/      # CI/CD workflows
```

---

##  Usage

This library is used in:

- [`model-training`](https://github.com/remla25-team22/model-training) – for consistent data preparation during training
- [`model-service`](https://github.com/remla25-team22/model-service) – to preprocess input before prediction

It is installed via a **versioned Git tag** in each dependent repository, for example:

```text
git+https://github.com/remla25-team22/lib-ml.git@v1.0.0
```
