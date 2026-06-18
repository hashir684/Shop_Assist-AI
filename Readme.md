# ShopAssist AI — Fine-Tuned Ecommerce Customer Support Assistant

ShopAssist is an AI-powered ecommerce customer support assistant. The goal of this project is to fine-tune a small open-source LLM to generate professional customer support responses for ecommerce queries.

## Current Phase

### Phase 1: Dataset Preparation

In this phase, we created a customer support dataset in JSONL format.

Each example contains:

- instruction
- input
- output
- category

## Categories

- Late Delivery
- Refund Request
- Return Request
- Order Cancellation
- Wrong Product
- Damaged Product
- Payment Issue
- Product Information
- Account/Login Issue
- Warranty Claim
- General Support

## Files

- `data/dataset.jsonl` — original dataset
- `data/support_sft.jsonl` — formatted dataset for supervised fine-tuning
- `training/validate_dataset.py` — validates dataset
- `training/prepare_sft_dataset.py` — converts dataset into SFT format

## Planned Features

- Fine-tuned LLM using LoRA/PEFT
- RAG-based ecommerce policy retrieval
- FastAPI backend
- Streamlit frontend
- Docker deployment