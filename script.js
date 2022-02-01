function printer(lst) {

  for (let i = 0; i < lst.length; i++) {

      const box = document.createElement("div");
      box.classList.add("box");
      const book = document.createElement("ul");
      const title = document.createElement("li");
      const author = document.createElement("li");
      const price = document.createElement("li");
      const urlEl = document.createElement("li");
      const url = document.createElement("button");
      title.innerText = "Title: " + lst[i].title;
      price.innerText = "Price: ₹" + lst[i].price;
      author.innerText = "Author: " + lst[i].author;
      url.innerText = "Link";
      url.onclick = function() {
        window.open(lst[i].url)
      }

      box.appendChild(book);
      book.appendChild(title);
      book.appendChild(author);
      book.appendChild(price);
      
      book.appendChild(urlEl)
      urlEl.appendChild(url);
      results = document.querySelector(".results")
      results.appendChild(box);

  }

//   console.log(inp);

}

async function fetcher(inp) {
    resultsbox = document.querySelector(".results")
    resultsbox.innerHTML = "";
    const loading = document.createElement("h3");
    loading.innerText = "Loading results...";
    
    resultsbox.appendChild(loading);
    await fetch('/getResults/' + inp, {
        keepalive: true
    })
        .then(res => res.json())
        
        .then(data => {
            
            
            loading.innerText = "Results: ";
            // loading.innerText = data.term;
            resultsbox.appendChild(loading);
            console.log(data)
            printer(data)
        });
}

function searcher() {

  const inp = document.querySelector("#search-bar");
  if (inp.value === "") {
      alert("Enter a query");
  } else {
      
      window.location.href = '/results/' + inp.value;
      inp.value = "";
      

  }
}




const search_btn = document.querySelector(".search-button");

document.querySelector("#search-bar").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      search_btn.click();
    }
  });

  search_btn.onclick = () => searcher();

const url = String(window.location.href)
if (url.includes("results")) {
  
  fetcher(url.slice(url.search('results/') + 8, ))
}


