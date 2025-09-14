const postsDiv = document.getElementById("posts");
const form = document.querySelector("form");
const searchiItemnput = form.children.searchItem;


const fetchinfo = async (item) => {
    try {
        console.log(item);
        const response = await fetch(`https://dummyjson.com/posts/search?q=${item}`);
        const data = await response.json();
        renderinfo(data);
    } catch (error) {
        console.log("error: " + error);
    }
};

function renderinfo(data) {
    postsDiv.innerHTML = "";
    const posts = data.posts;
    for (let i = 0; i < posts.length; i++) {
        const post = posts[i];
        postsDiv.innerHTML += `
        <div>
            <h2>${post.title}</h2>
            <p>${post.body}</p>
        </div>
        `;
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    fetchinfo(searchiItemnput.value);
})