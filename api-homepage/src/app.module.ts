import { Module } from '@nestjs/common';

import { MoviesController } from './movies/movies.controller';
import { TestController } from './test/test.controller';

@Module({
  imports: [],
  controllers: [MoviesController, TestController],
  providers: [],
})
export class AppModule {}
