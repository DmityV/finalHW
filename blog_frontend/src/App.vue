<template>
  <header>
    <div class="pannel">
      <button class="button-create-post" @click="showPostCreate = true">Создать пост</button>
      <PostCreate v-if="showPostCreate" @close="showPostCreate = false" :addPosts = "addPosts">
        <h2>Создать пост</h2>
        <p><input class="post-create-input" type="text" v-model="new_title" placeholder="Заголовок"></p>
        <p><textarea class="post-create-textarea" v-model="new_content" placeholder="Текст поста"></textarea></p>
      </PostCreate>  
    </div>
  </header>
  <post-list :posts="posts" :fetchPosts="fetchPosts"/>
</template>

<script>
import PostList from './components/PostList.vue';
import PostCreate from './components/PostCreate.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    PostList,
    PostCreate
  },
  data() {
    return {
      posts: [],
      new_title: "",
      new_content: "",
      showPostCreate: false
    }
  },
  created() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('/api/posts/');
        this.posts = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async addPosts() {
      try {
        await axios.post('/api/posts/', {
          title: this.new_title,
          content: this.new_content
        });
        this.new_title = "";
        this.new_content = "";
      } catch (error) {
        console.log(error);
      }
      this.showPostCreate = false;
      this.fetchPosts()
    }
  }
}
</script>

<style>
* {
  font-family: sans-serif;
  box-sizing: border-box;
  font-size: 16px;
}
h2 {
  margin: 10px 0;
  font-size: 32px;
  font-weight: normal;
  color: #666666;
}
header {
  height: 50px;
  text-align: right;
  border-bottom: solid rgb(221, 221, 221) 1px;
}
button {
  cursor: pointer;
  width: 150px;
  height: 40px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
}
.pannel {
  margin: 0 auto;
  width: 80%;
}
.button-create-post {
  background-color: rgb(39, 130, 59);
  color: white;
}
.post-create-textarea {
  width: 100%;
  padding: 10px;
  height: 150px;
  border: 1px solid #d3d3d3;
}
.post-create-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #d3d3d3;
}
</style>
