/*
   Opportunities Finder – Version 1 (simple JavaScript)
   Lesson 4: variables, functions, loops, conditions and events

   The cards are already written in index.html. This script has one job:
   SHOW or HIDE them when someone chooses a topic.

     1. Find the things on the page we need           (variables)
     2. A function that answers "does this card match?" (parameters + return)
     3. A function that checks every card              (loop + if)
     4. Listen for the form being submitted            (event)
*/

/*  STEP 1: FIND THE HTML ELEMENTS 
   document.querySelector("#topic") means "find the element with id="topic"".
   document.querySelectorAll(".card") means "find EVERY element with class="card"".
   We store each result in a const (a variable that will not change) so we can use it later. */
const form = document.querySelector("#filter-form");
const topicSelect = document.querySelector("#topic");
const message = document.querySelector("#results-message");
const cards = document.querySelectorAll(".card");

/*  STEP 2: A FUNCTION 
   A function is a reusable recipe:
     INPUTS   (parameters)  →  what it needs
     ACTIONS                →  what it does
     OUTPUT   (return)      →  what it gives back

   cardMatches(card, topic)
     Inputs:  one card, and the topic we are looking for (like "tech")
     Output:  true if the card should be shown, false if it should be hidden

   In the HTML, a card has data-category="tech".
   In JavaScript, that is card.dataset.category. */
function cardMatches(card, topic) {
  if (topic === "all") {
    return true; // "all" means every card matches
  }
  return card.dataset.category === topic; // === asks "are these exactly the same?"
}

/*  STEP 3: A LOOP AND A DECISION 
   showTopic(topic) checks every card, then tells the person what happened. */
function showTopic(topic) {
  let visibleCount = 0; // "let" is for a variable that WILL change

  // "for...of" means: for each card in the list, run the code in the braces.
  for (const card of cards) {
    if (cardMatches(card, topic)) {
      card.hidden = false; // show it
      visibleCount = visibleCount + 1; // count it
    } else {
      card.hidden = true; // hide it
    }
  }

  // A DECISION: what should we tell the person?
  if (visibleCount === 0) {
    message.textContent =
      "No opportunities in this topic yet. Try another topic!";
  } else {
    message.textContent =
      "Showing " + visibleCount + " of " + cards.length + " opportunities.";
  }
}

/*  STEP 4: EVENTS – MAKE IT RESPOND 
   addEventListener("submit", function) means:
   "When the form is submitted, run this function."
   Pressing the button OR pressing Enter both count as submitting. */
form.addEventListener("submit", function (event) {
  event.preventDefault(); // stop the browser reloading the page
  showTopic(topicSelect.value); // .value is whatever option is chosen, e.g. "tech"
});

/*  STEP 5: START 
   Run once when the page loads so the message is filled in. */
showTopic("all");

/*  TRY IT YOURSELF 
   1. Copy one whole <article class="card"> in index.html and paste it after the last one.
      Change the words. Refresh. Does the message say 9 of 9?
   2. Set data-category="volunteer" on your new card, then choose "Volunteering".
      What happened to the "No opportunities" message?
   3. Open the Console and type:  cards.length
      then:  cardMatches(cards[0], "study")
      then:  cardMatches(cards[0], "tech")
   4. Change data-category="tech" to data-category="Tech" on one card.
      Why does it disappear from the Tech filter? (Hint: capital letters matter.) */
