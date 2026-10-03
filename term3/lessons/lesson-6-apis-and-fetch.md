# Lesson 6 – APIs and Fetching Data from the Internet

**Term:** 3 · Holiday self-study (week 2)  
**Time:** About 2–3 hours, split into shorter sessions  
**Audience:** Grade 10 students, Alliance Girls High School  
**Tools:** Browser, CodePen, and [Open-Meteo](https://open-meteo.com/) (free; no API key)

> 🏠 **Take-home lesson:** Work through these steps on your own during the holiday. Read the
> [Holiday Self-Study Pack](../holiday-self-study.md) first.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Explain an API request and response using a restaurant-order analogy.
2. Read a small JSON response.
3. Fetch public data with `fetch`, `async`, and `await`.
4. Show loading, success, empty, and error states.

## Self-Study Steps

### Step 1 | Connect: Ask Another Service for Data

An API is like ordering at a restaurant: your page sends a **request**, and the kitchen (the API)
sends back a **response**. Copy this flow into your journal:

```text
Our page → request → API
Our page ← JSON response ← API
```

Write one reason why you should never publish a secret API key or send private personal data to an
API.

### Step 2 | Learn: Fetch Current Weather

In a new CodePen, add `<p id="weather-status"></p>` to the HTML panel. Then paste this into the
JavaScript panel. It uses Open-Meteo's no-key endpoint with Nairobi coordinates:

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

Open the API address in a new browser tab to see the raw JSON. Find the two values the page uses.

### Step 3 | Experiment

Try each change, then check the result:

1. Change the coordinates to another Kenyan town.
2. Add one more current-weather field from the [API documentation](https://open-meteo.com/en/docs).
3. Add a **Refresh** button that calls `loadWeather()` again.
4. Temporarily break the URL to confirm the error message appears.
5. Restore the URL and confirm the page recovers.

### Step 4 | Responsible API Use

Read these four rules and copy them into your journal:

- Read the API's documentation and usage limits.
- Do not commit secret keys.
- Request only the data the page needs.
- Design a useful fallback when the service or internet is unavailable.

### Step 5 | Capstone Checkpoint

Add fetched data to your own capstone:

| Capstone | Data to fetch |
|---|---|
| School Opportunities Hub | Your own `opportunities.json` file |
| Kenya Weather Dashboard | Open-Meteo current weather for your chosen locations |
| CyberSmart Quest | Your own `questions.json` file |

Your feature must show a loading message, a friendly error message, and an empty state, never a
blank screen. In CodePen, you can keep the JSON in an array until Lesson 7, then move it into its
own file in your repository.

### Step 6 | Learning Journal

Draw the request/response flow for your capstone and explain, in your own words, what `await` and
`try/catch` do.

✅ **Done when:** your capstone displays fetched (or clearly labelled sample) data with loading and
error states, and your journal entry is complete.

## Free Practice

- [MDN: Fetching data from the server](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Network_requests)
- [Open-Meteo documentation](https://open-meteo.com/en/docs)
- [JSONPlaceholder practice API](https://jsonplaceholder.typicode.com/)

## Facilitator Notes

- Before the holiday, share sample JSON that students can use as an offline fallback.
- Do not ask students to enter payment details for a "free trial."
- Avoid APIs that require publishing a key in browser code.

