fetch("https://rawg-video-games-database.p.rapidapi.com/games", {
        method: "GET",
        headers: {
            "x-rapidapi-host": "rawg-video-games-database.p.rapidapi.com",
            "x-rapidapi-key": "8411cc8516msha2a3ca0bc2e16d5p1dad95jsn240bd1cc5f66",
        },
    })
    .then((dataWrappedByPromise) => dataWrappedByPromise.json())
    .then((data) => {
            var body = null;
            body = data.results;
            console.log(body);
            document.getElementById("Games").innerHTML = `
        <h1>${body
          .map(function (game) {
            return `
            <div id="align">
              <div id="test">
                <p1 class="gamename">${game.name}</p1><p1 class="ratings">Rating: ${game.rating}</p1><br>
                <img class="pictures" alt="${game.name}" src="${game.background_image}">
              </div>
            </div>
            `;
          })
          .join("")}<h1/>
      `;
  });