var currentPage = 1;
var postsPerPage = 10;

function getPosts(page) {
    currentPage = page || currentPage;

    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => response.json())
        .then(data => {
            var posts = data;
            var visiblePosts = posts.slice((currentPage - 1) * postsPerPage, currentPage * postsPerPage);
            displayPosts(visiblePosts);
            updatePagination(posts);
        });
}

function displayPosts(posts) {
    var postsContainer = document.getElementById('posts-container');
    postsContainer.innerHTML = '';

    var commentPromises = posts.map(post => {
        return fetch(`https://jsonplaceholder.typicode.com/posts/${post.id}/comments`)
            .then(response => response.json())
            .then(comments => {
                post.comments = comments;
            });
    });

    Promise.all(commentPromises).then(() => {
        posts.forEach(post => {
            var postElement = document.createElement('div');
            postElement.classList.add('post');
            postElement.innerHTML = `
                <div class="alert alert-warning">
                    <p class="post_number">Пост № ${post.id}</p>
                    <h2>Заголовок поста: ${post.title}</h2>
                    <p>Текст поста: ${post.body}</p>
                    <button class="btn btn-primary" onclick="toggleComments(this)">Показать комментарии</button>
                    <div class="post-comments" style="display: none;">
                        <ul>
                            ${post.comments.map(comment => `
                                <li>
                                    <div class="comment1">
                                        <b>Пользователь:</b> ${comment.name}<br>
                                        <b>Почта:</b> ${comment.email}<br><br>
                                        <b>Комментарий:</b> ${comment.body}<br>
                                    </div>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>
            `;

            postsContainer.appendChild(postElement);
        });
    });
}

function toggleComments(button) {
    var comments = button.parentElement.querySelector('.post-comments');
    comments.style.display = comments.style.display === 'none' ? 'block' : 'none';

    var buttonText = button.textContent;

    if (buttonText === 'Скрыть комментарии') {
        button.textContent = 'Показать комментарии';
    } else {
        button.textContent = 'Скрыть комментарии';
    }
}

function updatePagination(posts) {
    var pages = Math.ceil(posts.length / postsPerPage);

    var paginationContainer = document.getElementById('pagination-container');
    paginationContainer.innerHTML = '';


    for (var i = 1; i <= pages; i++) {
        var pageButton = document.createElement('button');
        pageButton.classList.add('button1');
        pageButton.textContent = i;

        if (i == currentPage) {
            pageButton.classList.remove('button1');
            pageButton.classList.add('active');
        }

        pageButton.addEventListener('click', function() {
            currentPage = parseInt(this.textContent);
            getPosts();
        });

        paginationContainer.appendChild(pageButton);

    }
}
getPosts();
updatePagination();