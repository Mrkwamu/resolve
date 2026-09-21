import { Module } from '@nestjs/common';

import { BrowserModule } from './browser/browser.module';
import { AppController } from './app.controller';

@Module({
  imports: [BrowserModule],
  controllers: [AppController],
  providers: [],
})
export class AppModule {}
