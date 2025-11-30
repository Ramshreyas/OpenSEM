# OpenSEM MVP Progress Tracker

This file breaks down the MVP implementation into fine-grained, actionable tasks. As tasks are completed, mark them as **[x]** and add notes as needed. The structure supports multiple SEM projects using shared scaffolding.

---

## 1. Project Setup
[x] Create base directory structure for multi-SEM support
[x] Add `.gitignore` for Python, Node.js, model files, and data
[x] Initialize git repository
[x] Create `requirements.txt` and install base dependencies
[x] Create template configs (`train_config.yaml`, `eval_config.yaml`)
[x] Create `scripts/` folder for utility scripts (e.g., new project creation, data formatting)
[x] Plan CLI app (`opensem-cli`) for project and workflow management
[x] Design CLI commands: `init`, `new-project`, `run-forge`, `train`, `evaluate`, etc.
[x] Implement basic CLI app structure in `src/` or as standalone entry point
[ ] Create README
[ ] Update README

## 2. Data Forge - Setup
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Implement data ingestion from `data/raw` (support .txt, .md)
[ ] Integrate external API for instruction/output synthesis
[ ] Allow teacher model configuration (e.g., GPT-4o, GPT-4o-mini)
[ ] Format output to JSONL (ShareGPT format)
[ ] Implement train/test split (90/10)
[ ] Save processed data to `data/processed` per SEM project
[ ] Update CLI
[ ] Update README

## 3. Data Forge - Trial/Test Domain
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Select a test domain (e.g., medical, legal, technical)
[ ] Populate `data/raw` with sample documents
[ ] Run synthesis to create training pairs
[ ] Create and verify a golden set in `data/golden`
[ ] Validate processed data format and quality
[ ] Update CLI
[ ] Update README

## 4. Training Floor - Baseline Test Creation
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Implement baseline evaluation using `judge.py`
[ ] Integrate Promptfoo for baseline scoring
[ ] Use vanilla base model (e.g., Llama-3.2-3B)
[ ] Iterate on baseline test prompts and golden set
[ ] Document baseline results
[ ] Update CLI
[ ] Update README

## 5. Finetune - Local/Cloud
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Implement hardware detection (local/cloud)
[ ] Configure Unsloth for training (YAML-driven)
[ ] Enforce VRAM limits for local (4090)
[ ] Enable full utilization for cloud (A100/H100)
[ ] Save LoRA adapters to `models/adapters/{run_name}` per SEM
[ ] Track training runs with Weights & Biases
[ ] Update CLI
[ ] Update README

## 6. Test Against Baseline
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Load fine-tuned adapter and rerun evaluation
[ ] Compare fine-tuned results to baseline
[ ] Update CLI
[ ] Output CLI summary table
[ ] Update README

## 7. Iterate Finetune & Test
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Refine training parameters/configs
[ ] Repeat finetuning and evaluation for improved results
[ ] Document iterations and findings
[ ] Update CLI
[ ] Update README

## 8. Report Generation
[ ] Discuss implementation plan
[ ] Update requirements.txt for phase
[ ] Generate performance report (accuracy, improvement %)
[ ] Summarize results for each SEM project
[ ] Document lessons learned and next steps
[ ] Update CLI
[ ] Update README

---

**Notes:**
- Each SEM project should have its own subdirectory under `data/`, `models/`, and configs, but share core scripts and logic.
- Update this file regularly as tasks are completed or requirements change.
