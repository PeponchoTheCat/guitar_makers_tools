# Guitar Maker Tools — progetto V1

## Scopo

Guitar Maker Tools è un'applicazione terminale per supportare le prime fasi di
progettazione di una chitarra. La V1 calcola le quote teoriche della tastiera
secondo il temperamento equabile, riducendo gli errori derivanti dal sommare
manualmente gli spazi tra tasti.

L'utente previsto è un liutaio o un progettista che necessita di una tabella
consultabile ed esportabile prima del tracciamento o del taglio delle cave.

## Funzioni incluse

- Calcolo della posizione di ogni tasto per una scala nominale e un numero di
  tasti scelto dall'utente.
- Per ogni tasto: distanza dal capotasto, spazio rispetto al tasto precedente
  e lunghezza vibrante residua.
- Calcolo inverso della scala da distanza nota e numero del tasto.
- Preset delle scale nominali comuni.
- Esportazione della tabella in CSV o testo formattato.

L'interfaccia e i messaggi sono in inglese. Gli input della V1 sono
esclusivamente in millimetri.

I preset includono le scale Martin standard (25,4 in) e short scale (24,9 in),
oltre alle Taylor standard (25,5 in) e GS Mini (23,5 in).

## Convenzione di misura e formule

La quota di ogni tasto è misurata dal bordo del capotasto rivolto verso il
ponte, lungo la linea teorica della corda. Per una scala `L` e un tasto
`n >= 1`:

```text
position(n) = L * (1 - 2 ^ (-n / 12))
residual(n) = L / 2 ^ (n / 12)
spacing(n)  = position(n) - position(n - 1)
scale       = position(n) / (1 - 2 ^ (-n / 12))
```

Le formule e gli esempi di riferimento sono descritti in
[`rapporto_scala_posizione_tasti.md`](rapporto_scala_posizione_tasti.md).
Il dodicesimo tasto deve risultare esattamente a metà della scala entro la
precisione di calcolo configurata.

## Flusso dell'interfaccia

La schermata Textual offre due aree:

1. **Fret calculator**: preset opzionale, scala in mm e numero intero positivo
   di tasti; il risultato è una tabella. Il dodicesimo tasto è evidenziato in
   giallo e il quattordicesimo in magenta.
2. **Inverse calculator**: numero del tasto e sua distanza dal capotasto in
   mm; il risultato è la scala teorica.

L'area export richiede un percorso di output, un selettore CSV/testo e un
pulsante di esportazione per creare il formato scelto dalla tabella corrente.
Gli errori di validazione o scrittura sono mostrati all'utente; non vengono
generati risultati o file parziali.

## Architettura

- `calculations/fretboard.py`: modelli e formule pure.
- `presets.py`: scale comuni centralizzate.
- `exporters.py`: serializzazione CSV e testo.
- `ui/app.py`: composizione e gestione della UI Textual.
- `__main__.py`: comando di avvio.

Il dominio non dipende da Textual. La precisione numerica usa `Decimal`;
l'arrotondamento a tre decimali è applicato alla tabella e a tutti i formati
di export.

## Criteri di accettazione

- Per 647,7 mm, le posizioni note (incluso il dodicesimo a 323,85 mm) sono
  coerenti con la documentazione.
- Per 630 mm, il settimo tasto è circa 209,53 mm.
- Input non finiti, non positivi o numero di tasto non intero/non positivo
  sono rifiutati con un messaggio esplicito.
- Il CSV contiene intestazioni e valori per ogni tasto; il testo è leggibile
  in terminale o in stampa.
- Il calcolo inverso ricostruisce la scala di origine con precisione
  sufficiente al dominio.

## Limiti della V1

Non sono inclusi compensazione di intonazione al ponte, multiscala/fanned
frets, conversione in pollici, tensione delle corde, azione, dimensionamento
della tastiera o sagoma dello strumento. Le quote non sostituiscono la verifica
metrologica, la dima di taglio o la decisione professionale del liutaio.
