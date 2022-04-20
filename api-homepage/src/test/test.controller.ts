import { Body, Controller, Delete, Get, Param, Patch, Post, Query } from '@nestjs/common';

@Controller('test')
export class TestController {
    //getHell(URL(생략가능)): string
    //함수명: 반환타입
    @Get('/123')
    getAll(): string {
        return 'hello';
    }
    // /test/search?year=2000
    @Get('search')
    search(@Query('year') seachingYear: string) {
        return `search year : ${seachingYear}`;
    }
    //매개변수 받고 출력 /test/123123123
    @Get('/:id')
    getParam(@Param('id') parameter: string) {
        return `param : ${parameter}`;
    }
    //post로 create 규칙진행
    @Post()
    create(@Body() movieData) {
      return movieData;
    }
    //delete로 규칙진행
    @Delete(':id')
    remove(@Param('id') movieId: string) {
      return `This will delete a movie with the id: ${movieId}`;
    }
    //patch로 규칙진행 test/321232 patch
    @Patch(':id')
    patch(@Param('id') movieId: string, @Body() updateData) {
      return {
        updatedMovie: movieId,
        ...updateData,
      };
    }
}
