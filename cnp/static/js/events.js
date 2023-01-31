let events = document.querySelectorAll("#upcoming-events li");

for (let i = 0; i < events.length; i++) {
  let event = events[i];

  event.addEventListener("mouseenter", function() {
    event.style.backgroundColor = "#f4f4f4";
  });

  event.addEventListener("mouseleave", function() {
    event.style.backgroundColor = "#fff";
  });
}
