# Sofascore Scraper API

API do scrapowania danych piłkarskich z Sofascore - gotowe do wdrożenia na RapidAPI.

## Szybki start

```bash
npm install
cp .env.example .env
# Ustaw API_KEY w .env
npm start
```

Serwer domyślnie na porcie `3000`.

## Autoryzacja

Wszystkie requesty wymagają nagłówka:

```
X-RapidAPI-Proxy-Secret: twój-klucz-api
# lub
X-API-Key: twój-klucz-api
```

Klucz ustawiasz w zmiennej `API_KEY` w pliku `.env`.

## Rate Limiting

Domyślnie: **30 requestów na minutę**. Możesz zmienić w `server.js`.

---

## Endpointy

### Turnieje / Ligi

| Metoda | Ścieżka | Opis |
|--------|---------|------|
| GET | `/api/tournaments/categories` | Lista kategorii (kraje) |
| GET | `/api/tournaments/categories/:id/tournaments` | Ligi w danej kategorii |
| GET | `/api/tournaments/tournaments` | Wszystkie dostępne turnieje |
| GET | `/api/tournaments/tournaments/:id` | Szczegóły turnieju |
| GET | `/api/tournaments/tournaments/:id/seasons` | Sezony turnieju |
| GET | `/api/tournaments/tournaments/:id/season/:seasonId/standings` | Tabela ligowa |
| GET | `/api/tournaments/tournaments/:id/season/:seasonId/top-players` | Top zawodnicy |

### Mecze

| Metoda | Ścieżka | Opis |
|--------|---------|------|
| GET | `/api/matches/live` | Aktualnie trwające mecze |
| GET | `/api/matches/date/:date` | Mecze w danym dniu (format: `YYYY-MM-DD`) |
| GET | `/api/matches/:eventId` | Szczegóły meczu |
| GET | `/api/matches/:eventId/incidents` | Wydarzenia meczowe (bramki, kartki) |
| GET | `/api/matches/:eventId/statistics` | Statystyki meczu |
| GET | `/api/matches/:eventId/lineups` | Składy drużyn |
| GET | `/api/matches/:eventId/odds` | Kursy bukmacherskie |
| GET | `/api/matches/:eventId/h2h` | Historia bezpośrednich spotkań |

### Drużyny

| Metoda | Ścieżka | Opis |
|--------|---------|------|
| GET | `/api/teams/search?q=nazwa` | Wyszukaj drużynę |
| GET | `/api/teams/:teamId` | Informacje o drużynie |
| GET | `/api/teams/:teamId/image` | Logo drużyny (URL) |
| GET | `/api/teams/:teamId/matches/next` | Nadchodzące mecze |
| GET | `/api/teams/:teamId/matches/last` | Ostatnie mecze |
| GET | `/api/teams/:teamId/transfers` | Transfery |
| GET | `/api/teams/:teamId/statistics/:tournamentId/:seasonId` | Statystyki w turnieju |

---

## Przykłady użycia

### Pobierz live mecze

```bash
curl -H "X-API-Key: test-key-123" http://localhost:3000/api/matches/live
```

### Pobierz mecze z dzisiaj

```bash
curl -H "X-API-Key: test-key-123" http://localhost:3000/api/matches/date/2025-07-12
```

### Pobierz szczegóły meczu

```bash
curl -H "X-API-Key: test-key-123" http://localhost:3000/api/matches/12345678
```

### Pobierz tabelę Premier League (sezon 52186 = 2024/25)

```bash
curl -H "X-API-Key: test-key-123" http://localhost:3000/api/tournaments/tournaments/17/season/52186/standings
```

### Wyszukaj drużynę

```bash
curl -H "X-API-Key: test-key-123" "http://localhost:3000/api/teams/search?q=Barcelona"
```

---

## Deployment na RapidAPI

1. Wdróż serwer na dowolnym hostingu (Render, Railway, VPS, Heroku)
2. W RapidAPI Hub wejdź w **My APIs > Add API**
3. Jako **API Provider Base URL** podaj URL swojego serwera
4. W **API Proxy Configuration** ustaw:
   - Header Name: `X-RapidAPI-Proxy-Secret`
   - Secret: ten sam klucz co `API_KEY` w `.env`
5. Skonfiguruj endpointy i plan cenowy

---

## Struktura projektu

```
rapidapiscraper/
  server.js              - główny plik serwera
  middleware/
    auth.js              - autoryzacja API key
  routes/
    matches.js           - endpointy meczów
    tournaments.js       - endpointy turniejów/lig
    teams.js             - endpointy drużyn
  services/
    sofascore.js         - klient HTTP do Sofascore API
    matches.js           - logika scrapowania meczów
    tournaments.js       - logika scrapowania turniejów
    teams.js             - logika scrapowania drużyn
  package.json
  .env.example
```

## Uwagi

- Sofascore może blokować zbyt częste zapytania - zachowaj rozsądny rate limit
- ID turniejów i drużyn znajdziesz eksplorując endpointy `/api/tournaments` i `/api/teams/search`
- Dane dostarczane "as is" - nie ponoszę odpowiedzialności za ich wykorzystanie
