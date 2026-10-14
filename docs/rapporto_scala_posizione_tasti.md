# Lunghezza della scala e posizione dei tasti sulla chitarra

## 1. Il rapporto tra scala e posizione dei tasti

Sulla chitarra, la distanza dei tasti dal capotasto dipende dalla **lunghezza della scala** (*scale length*), cioè dalla distanza teorica tra il capotasto e il punto di appoggio della corda sul ponte, prima di considerare la compensazione d'intonazione.

La posizione dei tasti non è distribuita in modo lineare: andando verso il ponte, gli spazi tra un tasto e il successivo diventano progressivamente più piccoli. Questo avviene perché ogni semitono della scala temperata divide la lunghezza vibrante residua per un fattore costante.

## 2. La formula per calcolare la posizione di un tasto

La distanza teorica del tasto numero \(n\), misurata dal bordo di riferimento del capotasto, è:

\[
\boxed{d_n = L\left(1-2^{-n/12}\right)}
\]

Dove:

- \(d_n\) = distanza dal capotasto al tasto numero \(n\);
- \(L\) = lunghezza della scala;
- \(n\) = numero del tasto, contando il primo come tasto 1;
- \(2^{-n/12}\) = fattore che deriva dalla divisione dell'ottava in 12 semitoni uguali.

La formula restituisce la posizione teorica del tasto lungo il manico. Per usarla, \(L\) e \(d_n\) devono essere espressi nella stessa unità di misura, ad esempio millimetri.

### Lunghezza vibrante residua

La lunghezza vibrante teorica della corda dopo aver premuto il tasto \(n\) è:

\[
\boxed{L_n = \frac{L}{2^{n/12}}}
\]

Di conseguenza, la posizione del tasto si ottiene sottraendo la lunghezza vibrante residua dalla scala iniziale:

\[
d_n = L-L_n
\]

## 3. Perché la formula funziona

Una corda ideale, mantenuta alla stessa tensione e con la stessa densità lineare, ha una frequenza fondamentale inversamente proporzionale alla sua lunghezza vibrante:

\[
f = \frac{1}{2L}\sqrt{\frac{T}{\mu}}
\]

Dove:

- \(f\) = frequenza fondamentale;
- \(L\) = lunghezza vibrante;
- \(T\) = tensione della corda;
- \(\mu\) = densità lineare della corda, cioè massa per unità di lunghezza.

Per salire di un'ottava, la frequenza deve raddoppiare. Per ottenere questo risultato, nel modello ideale la lunghezza vibrante deve dimezzarsi. L'ottava viene divisa in dodici semitoni uguali nella scala temperata: ogni semitono moltiplica la frequenza per \(2^{1/12}\), e quindi riduce la lunghezza vibrante per il fattore inverso \(2^{-1/12}\).

Dopo \(n\) semitoni:

\[
L_n = L\left(2^{-1/12}\right)^n = \frac{L}{2^{n/12}}
\]

La posizione del tasto è la differenza tra la scala iniziale e la lunghezza residua, da cui deriva la formula principale.

## 4. Distanza tra due tasti consecutivi

La distanza tra il tasto \(n-1\) e il tasto \(n\) è:

\[
\boxed{\Delta d_n = d_n-d_{n-1}
= L\,2^{-(n-1)/12}\left(1-2^{-1/12}\right)}
\]

La formula mostra che la distanza tra tasti consecutivi diminuisce in modo geometrico. Il rapporto tra uno spazio e quello immediatamente precedente è costante:

\[
\boxed{\frac{\Delta d_{n+1}}{\Delta d_n}=2^{-1/12}\approx 0{,}943874}
\]

In pratica, ogni intervallo è circa il **94,39%** del precedente, cioè è più corto di circa il **5,61%** rispetto allo spazio immediatamente precedente.

## 5. Esempio: scala da 647,7 mm

Una scala di **647,7 mm** corrisponde a 25,5 pollici, misura tipica delle Fender Telecaster e Stratocaster.

Applicando la formula:

\[
d_n = 647{,}7\left(1-2^{-n/12}\right)
\]

si ottengono, arrotondando al centesimo di millimetro, le seguenti posizioni teoriche:

| Tasto | Distanza dal capotasto (mm) |
|---:|---:|
| 1 | 36,35 |
| 2 | 70,66 |
| 3 | 103,05 |
| 4 | 133,62 |
| 5 | 162,47 |
| 6 | 189,71 |
| 7 | 215,41 |
| 8 | 239,67 |
| 9 | 262,58 |
| 10 | 284,19 |
| 11 | 304,59 |
| 12 | 323,85 |
| 13 | 342,03 |
| 14 | 359,18 |
| 15 | 375,38 |
| 16 | 390,66 |
| 17 | 405,09 |
| 18 | 418,70 |
| 19 | 431,56 |
| 20 | 443,69 |
| 21 | 455,14 |
| 22 | 465,95 |

Il dodicesimo tasto si trova esattamente a metà della scala teorica:

\[
d_{12}=L\left(1-\frac{1}{2}\right)=\frac{L}{2}
\]

Nel caso dell'esempio:

\[
d_{12}=\frac{647{,}7}{2}=323{,}85\ \text{mm}
\]

Questo è un controllo utile per verificare rapidamente un calcolo o un disegno.

## 6. Esempio con una scala da 630 mm

Per una scala di **630 mm**, la posizione del settimo tasto è:

\[
d_7=630\left(1-2^{-7/12}\right)\approx 209{,}53\ \text{mm}
\]

Quindi il settimo tasto si trova teoricamente a circa **209,53 mm dal capotasto**.

## 7. Dalla teoria alla costruzione reale

La formula fornisce le posizioni teoriche dei tasti secondo il temperamento equabile e il modello di corda ideale. Nella costruzione e nel setup reali occorre tenere presenti alcuni aspetti.

### Riferimento di misura

La distanza va misurata dal punto di riferimento del capotasto, cioè dal lato rivolto verso il ponte, lungo la linea teorica della corda. Per la realizzazione di una tastiera, è importante mantenere un riferimento coerente in tutte le misure.

### Compensazione al ponte

La scala nominale non coincide sempre con la lunghezza effettiva della corda a vuoto una volta regolata la chitarra. Per compensare gli effetti della rigidità della corda, dell'azione e della pressione esercitata durante la diteggiatura, il punto di appoggio della corda al ponte viene normalmente arretrato rispetto alla posizione teorica. Questa regolazione è detta **compensazione d'intonazione** (*intonation compensation*).

La compensazione riguarda il punto di appoggio al ponte e non cambia la formula geometrica usata per posizionare i tasti.

### Precisione pratica

Per tracciare una tastiera, non è consigliabile accumulare le distanze tra tasti una dopo l'altra: un piccolo errore su ogni intervallo può sommarsi lungo il manico. È preferibile calcolare ogni posizione a partire dallo stesso riferimento del capotasto, oppure usare una dima o una procedura di misura precisa. In un lavoro di liuteria, anche la precisione del taglio delle cave e la larghezza effettiva della lama sono importanti.

## 8. Formula inversa: ricavare la scala da una posizione nota

Se si conosce la distanza \(d_n\) del tasto \(n\) dal capotasto e si vuole ricavare la lunghezza teorica della scala, si può riordinare la formula:

\[
d_n=L\left(1-2^{-n/12}\right)
\]

ottenendo:

\[
\boxed{L=\frac{d_n}{1-2^{-n/12}}}
\]

È utile, per esempio, per verificare la scala teorica di una tastiera esistente a partire da una misura affidabile.

## 9. Riepilogo

Le relazioni fondamentali sono:

**Posizione del tasto \(n\):**

\[
\boxed{d_n=L\left(1-2^{-n/12}\right)}
\]

**Lunghezza vibrante residua:**

\[
\boxed{L_n=\frac{L}{2^{n/12}}}
\]

**Spazio tra due tasti consecutivi:**

\[
\boxed{\Delta d_n=L\,2^{-(n-1)/12}\left(1-2^{-1/12}\right)}
\]

**Scala ricavata dalla posizione di un tasto:**

\[
\boxed{L=\frac{d_n}{1-2^{-n/12}}}
\]

Il principio essenziale è che la posizione dei tasti dipende dalla scala attraverso una progressione geometrica, non attraverso una divisione lineare del manico. Il dodicesimo tasto cade a metà della scala teorica; ogni semitono successivo riduce la lunghezza vibrante di un fattore costante.
