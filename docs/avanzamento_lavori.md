# Avanzamento lavori — Guitar Maker Tools V1

Questo documento rappresenta lo stato effettivo della roadmap della V1.

| Milestone | Stato | Dipendenze | Criterio di completamento |
|---|---|---|---|
| Documentazione di progetto | Completata | Nessuna | Specifica e roadmap presenti e allineate ai requisiti |
| Base del progetto Python | Completata | Documentazione di progetto | Pacchetto, dipendenze, test e comando di avvio configurati |
| Motore di calcolo e preset | Completata | Base del progetto Python | Formule, modelli, validazione e preset implementati |
| Test dominio ed export | Completata | Motore di calcolo e preset | Esempi teorici, validazioni e serializzazione coperti |
| UI Textual | Completata | Motore di calcolo e preset | Calcolo diretto e inverso usabili da terminale |
| Export integrato | Completata | UI Textual; Test dominio ed export | CSV e testo generabili dalla tabella corrente |
| Documentazione finale e verifica | Completata | Export integrato | README e stato aggiornati, controlli configurati superati |

## Log di avanzamento

- Documentazione iniziale, pacchetto Python e UI Textual completati.
- Il motore usa `Decimal` e calcola ogni posizione dal riferimento comune del
  capotasto; preset, calcolo inverso ed export CSV/testo sono disponibili.
- Corrette le quote di esempio della documentazione per renderle coerenti con
  la formula del temperamento equabile.
- Corretto il layout Textual affinché la tabella dei risultati resti visibile
  nel viewport standard di un terminale 80×24.
- Aggiunti pulsante **Quit** e scorciatoia `Q` per terminare l'applicazione.
- Reso interamente visibile il pulsante di calcolo e aggiunte evidenziazioni
  cromatiche per il dodicesimo e il quattordicesimo tasto.
- Riorganizzata l'area export con un selettore CSV/testo e controlli tutti
  visibili nel viewport standard.
- Uniformato l'arrotondamento a tre decimali per applicazione, export CSV e
  testo.
- Aggiunti preset Martin standard/short scale e Taylor standard/GS Mini.
- Rilasciata la versione iniziale 1.0.0 e aggiunto `CHANGELOG.md`.
- Aggiunto `.gitignore` per artefatti locali Python e aggiornato il README con
  i riferimenti alle risorse del progetto.
- Aggiunte al README schermate dell'applicazione per calcolo tasti e calcolo
  inverso.
- Verifica completata: `pytest -q` — 24 test superati.
