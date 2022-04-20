import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

//이름은 마음대로
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
