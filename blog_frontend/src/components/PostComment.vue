<template>
  <div class="comment">
    <p class="comment-body"><strong>{{ comment.author }}</strong>: {{ comment.content }}</p>
    <p class="comment-delete" @click="deleteComment(comment.id)">Удалить</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    comment: { type: Object },
    fetchPosts: { type: Function }
  },
  methods: {
    async deleteComment(idCommentForDelete) {
      try {
        await axios.delete('/api/comments/'+idCommentForDelete);
      } catch (error) {
        console.log(error);
      }
      this.fetchPosts()
    }
  }
}
</script>

<style scoped>
.comment-delete {
  cursor: pointer;
  color: red;
  text-decoration: underline;
  margin: 0;
}
.comment-body {
  margin-bottom: 5px;
}
</style>