import { IsString, IsNumber, IsOptional } from 'class-validator';

export class CreatePostDto {
  @IsString()
  readonly title: string;

  @IsNumber()
  readonly year: number;

  @IsOptional()
  @IsString({ each: true })
  readonly genres: string[];

  @IsString()
  readonly contents: string;

  @IsString()
  readonly url: string;
}