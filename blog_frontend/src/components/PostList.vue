<template>
  <div class="post-list">
	<p style="font-size: 52px; margin: 0 0 20px 0;">Список постов</p>
    <post-item v-for="post in posts" :key="post.id" :post="post" :fetchPosts="fetchPosts"/>
  </div>
</template>


<script>
	import PostItem from './PostItem.vue';

	export default {
		components: { PostItem },
		props: {
			posts: { type: Array },
			fetchPosts: { type: Function }
		}
	}
</script>

<style scoped>
.post-list {
	margin: 20px 40px;
	text-align: center;
	width: 1000px;
}
@media (max-width: 1040px) {
	.post-list {
		width: auto;
	}
}
</style>