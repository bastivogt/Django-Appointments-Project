const backLinks = document.querySelectorAll(".back-link");

for(let backLink of backLinks) {
    backLink.addEventListener("click", e => {
        e.preventDefault();
        window.history.back();
    });
}