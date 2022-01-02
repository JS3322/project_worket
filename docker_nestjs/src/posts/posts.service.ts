import { Injectable, NotFoundException } from '@nestjs/common';
import { HomePost } from './entities/homePost.entity';
import { CreatePostDto } from './dto/create-post.dto';
import { UpdatePostDto } from './dto/update-post.dto';

@Injectable()
export class PostsService {
  private posts: HomePost[] = [];

  getAll(): HomePost[] {
    return this.posts;
  }

getOne(id: number): HomePost {
    const post = this.posts.find(post => post.id === id);
    if (!post) {
      throw new NotFoundException(`post with ID ${id} not found.`);
    }
    return post;
  }

  deleteOne(id: number) {
    this.getOne(id);
    this.posts = this.posts.filter(post => post.id !== +id);
  }

  create(postData: CreatePostDto) {
    this.posts.push({
      id: this.posts.length + 1,
      ...postData,
    });
  }

  update(id: number, updateData: UpdatePostDto) {
    const post = this.getOne(id);
    this.deleteOne(id);
    this.posts.push({ ...post, ...updateData });
  }
}