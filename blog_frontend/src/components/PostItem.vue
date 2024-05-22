<template>
  <div class="post-item">

    <div v-if="editMode == false" class="post-body">
      <h2>{{ post.title }}</h2>
      <p class="post-content">{{ post.content }}</p>
    </div>

    <div v-if="editMode == true">
      <p><input class="post-create-input" type="text" v-model="edit_title"></p>
      <p><textarea class="post-create-textarea" v-model="edit_content"></textarea></p>
      <div class="edit-mode-buttons">
        <button class="edit-mode-send" @click="postEdited()">Отправить</button>
        <button class="edit-mode-cancel" @click="editMode = false">Отменить</button>
        <button class="edit-mode-delete" @click="deletePost(post.id)">Удалить</button>
      </div>
    </div>

    <div class="post-buttons">

      <div class="post-buttons-edit-delete" v-if="editMode == false" @class="post-related-buttons">
        <span class="post-edit" @click="editPost()">Изменить пост</span>
        <span> | </span>
        <span class="post-delete" @click="deletePost(post.id)">Удалить пост</span>
      </div>

      <div class="post-buttons-comments">
        <span class="comment-show" v-if="post.comments.length != 0 && showComments == false" @click="showComments = true">
          Показать комментарии ({{ post.comments.length }})</span>
        <span class="comment-show" v-else-if="post.comments.length != 0 && showComments == true" @click="showComments = false">
          Скрыть комментарии ({{ post.comments.length }})</span>
        <span v-if="post.comments.length != 0"> | </span>
        <span class="new-comment-send" v-if="showForm == false" @click="showForm = true">Комментировать</span>
        <span class="new-comment-send" v-if="showForm == true" @click="commentStop()"><span class="one-row">Не комментировать</span></span>
      </div>

    </div>

    <div class="comment-block" v-if="showComments == true">
      <Comment
        v-for="comment in post.comments"
        :key="comment.id"
        :comment="comment"
        :fetchPosts="fetchPosts"
      />
    </div>

    <div class="new-comment-form" v-if="showForm == true">
      <p><input type="text" v-model="comment_author" placeholder="Автор комментария"></p>
      <p class="new-comment-textarea"><textarea v-model="comment_content" placeholder="Текст комментария"></textarea></p>
      <div class="new-comment-buttons">
        <span class="new-comment-send" @click="commentPost(post.id)">Отправить комментарий</span> | <span class="new-comment-back" @click="commentStop(post.id)">Отменить</span> 
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import Comment from './PostComment.vue';

export default {
  components: { Comment },
  data() {
    return {
      // posts: [],
      edit_title: "",
      edit_content: "",
      edit_post: {},
      comment_author: "",
      comment_content: "",
      new_comment: {},
      showComments: false,
      showForm: false,
      editMode: false
    }
  },
  props: {
    post: { type: Object},
    fetchPosts: { type: Function }
  },
  methods: {
    editPost() {
      this.editMode = true;
      this.edit_title = this.post.title;
      this.edit_content = this.post.content
    },
    async postEdited() {
      try {
        await axios.patch('/api/posts/' + this.post.id + '/', {
          title: this.edit_title,
          content: this.edit_content
        });
      } catch (error) {
        console.log(error);
      }
      this.editMode = false;
      this.fetchPosts()
    },
    async deletePost(idForDelete) {
      try {
        await axios.delete('/api/posts/'+idForDelete);
      } catch (error) {
        console.log(error);
      }
      this.fetchPosts()
    },
    async commentPost(idForComment) {
      try {
        await axios.post('/api/comments/', {
          author: this.comment_author,
          content: this.comment_content,
          post: idForComment
        });
        this.comment_author = "";
        this.comment_content = "";
        this.showForm = false;
      } catch (error) {
        console.log(error);
      }
      this.fetchPosts();
      this.showComments = true
    },
    commentStop() {
      this.comment_author = "";
      this.comment_content = "";
      this.showForm = false;
    }
  }
}
</script>

<style scope>
.post-item {
  text-align: left;
  background-color: white;
  margin-bottom: 20px;
  padding: 20px;
  border: 1px solid #d3d3d3;
  border-radius: 8px;
}
.post-body {
  margin-bottom: 30px;
}
.post-content {
  color: #333333;
}

.comment-block {
  padding-top: 15px;
  margin-left: 40px;
}
.one-row {
  white-space: nowrap;
}

/* After post buttons */
.post-buttons {
  font-size: 16px;
  text-align: center;
  line-height: 1.6;
}
.post-delete {
  cursor: pointer;
  color: red;
  text-decoration: underline;
}
.post-edit {
  cursor: pointer;
  color: rgb(39, 130, 59);
  text-decoration: underline;
}
.comment-show {
  cursor: pointer;
  color: blue;
  text-decoration: underline;
}
.new-comment-send {
  cursor: pointer;
  color: rgb(39, 130, 59);
  text-decoration: underline;
}

/* Add comment */
.new-comment-form {
  margin-left: 30px;
  width: 500px;
  padding-top: 10px;
  padding-bottom: 15px;
}
@media (max-width: 650px) {
	.new-comment-form {
		width: auto;
	}
}
.new-comment-form input {
  font-size: 16px;
  width: 100%;
  padding: 5px;
  border: 1px solid #d3d3d3;
}
.new-comment-form textarea {
  font-size: 16px;
  border: 1px solid #d3d3d3;
  width: 100%;
  height: 100px;
  padding: 5px;
}
.new-comment-textarea {
  margin-bottom: 5px;
}
.new-comment-buttons {
  text-align: right;
}

.new-comment-back {
  cursor: pointer;
  text-decoration: underline;
}

/* Post edit mode */
.edit-mode-buttons {
  text-align: right;
  padding-bottom: 20px;
}
.edit-mode-send {
  background-color: rgb(39, 130, 59);
  color: white;
  margin-right: 10px;
}
.edit-mode-cancel {
  border: 1px solid rgb(221, 221, 221);
  background-color: white;
  margin-right: 10px;
}
.edit-mode-delete {
  background-color: rgb(213, 44, 44);
  color: white;
}
</style>