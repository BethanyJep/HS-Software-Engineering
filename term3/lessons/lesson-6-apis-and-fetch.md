# Lesson 6 – APIs and Fetching Data from the Internet

**Term:** 3  
**Duration:** 90 minutes  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, CodePen, and [Open-Meteo](https://open-meteo.com/) (free; no API key)

---

## Learning Objectives

Students will be able to:

1. Explain an API request and response using a restaurant-order analogy.
2. Read a small JSON response.
3. Fetch public data with `fetch`, `async`, and `await`.
4. Show loading, success, empty, and error states.

## Lesson Plan

### ⏱ 0–15 min | Connect: Ask Another Service for Data

Draw this flow:

```text
Our page → request → API
Our page ← JSON response ← API
```

Discuss why teams should never publish secret API keys or send private student data to an API.

### ⏱ 15–35 min | Learn: Fetch Current Weather

Use Open-Meteo's no-key endpoint with Nairobi coordinates:

```javascript
const status = document.querySelector("#weather-status");

async function loadWeather() {
  status.textContent = "Loading weather…";

  try {
    const response = await fetch(
      "https://api.open-meteo.com/v1/forecast?latitude=-1.2864&longitude=36.8172&current=temperature_2m"
    );

    if (!response.ok) {
      throw new Error(`Request failed: ${response.status}`);
    }

    const data = await response.json();
    status.textContent = `Nairobi: ${data.current.temperature_2m} ${data.current_units.temperature_2m}`;
  } catch (error) {
    status.textContent = "Weather is unavailable. Please try again later.";
    console.error(error);
  }
}

loadWeather();
```

Inspect the JSON in the console and identify the values used on the page.

### ⏱ 35–55 min | Guided Experiments

Students:

1. Change the coordinates to another city.
2. Add one more current-weather field from the API documentation.
3. Add a refresh button.
4. Temporarily break the URL to confirm the error message appears.
5. Restore the URL and confirm the page recovers.

### ⏱ 55–65 min | Responsible API Use

Review four rules:

- Read the API's documentation and usage limits.
- Do not commit secret keys.
- Request only the data the page needs.
- Design a useful fallback when the service or internet is unavailable.

### ⏱ 65–80 min | Capstone Checkpoint

Teams either add relevant public API data or build a clearly labelled sample-data fallback. The
feature must display a loading message and a friendly error message, not a blank screen.

### ⏱ 80–90 min | Exit Ticket

Students draw the request/response flow and explain what `await` and `try/catch` do.

## Free Practice

- [MDN: Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)
- [Open-Meteo documentation](https://open-meteo.com/en/docs)
- [JSONPlaceholder practice API](https://jsonplaceholder.typicode.com/)

## Facilitator Notes

- Test API access on the school network before class and keep sample JSON as an offline fallback.
- Do not ask students to enter payment details for a "free trial."
- Avoid APIs that require publishing a key in browser code.

