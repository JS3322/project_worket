import {
    Controller,
    Get,
    Param,
    Post,
    Delete,
    Patch,
    Body,
  } from '@nestjs/common';
  import { PostsService } from './posts.service';
import { HomePost } from './entities/homePost.entity';
import { CreatePostDto } from './dto/create-post.dto';
import { UpdatePostDto } from './dto/update-post.dto';

@Controller('posts')
export class PostsController {
    constructor(private readonly postsService: PostsService) {}

  @Get()
  getAll(): HomePost[] {
    return this.postsService.getAll();
  }

  @Get(':id')
  getOne(@Param('id') postId: number): HomePost {
    return this.postsService.getOne(postId);
  }

  @Post()
  create(@Body() postData: CreatePostDto) {
    return this.postsService.create(postData);
  }

  @Delete(':id')
  remove(@Param('id') postId: number) {
    return this.postsService.deleteOne(postId);
  }

  @Patch(':id')
  patch(@Param('id') postId: number, @Body() updateData: UpdatePostDto) {
    return this.postsService.update(postId, updateData);
  }
}