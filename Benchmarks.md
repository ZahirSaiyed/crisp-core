# Benchmarks

All runs use the **JFK 30‑second sample** (`samples/jfk.wav`) and Whisper cpp commit
`<commit‑hash>` unless noted.  
RTF = (real‑time seconds) ÷ (audio seconds).  RTF < 1 ⇒ faster than real‑time.

| Date       | Model         | Hardware / Image Tag        | Audio sec | Real‑time sec | RTF  | Cost $/min* | Notes            |
|------------|---------------|-----------------------------|-----------|---------------|------|-------------|------------------|
| 2025‑07‑30 | tiny.en (fp16)| **Docker CPU, Apple M1**    | 30        | **1.78**      | 0.06 | n/a         | Baseline, no GPU |
|            |               |                             |           |               |      |             |                  |

\*Cost $/min field stays “n/a” for local CPU; you’ll fill it in when you test cloud CPUs or GPUs.

---

## How to reproduce

```bash
# build image
docker build -t crisp-whisper:cpu .

# run (CPU)
docker run --rm -v $PWD/test-data:/audio \
  -w /opt/whisper.cpp/build/bin crisp-whisper:cpu \
  /opt/whisper.cpp/build/bin/whisper-cli \
    -m /opt/whisper.cpp/ggml-tiny.en.bin \
    -f /audio/test30.wav -otxt -of /audio/out