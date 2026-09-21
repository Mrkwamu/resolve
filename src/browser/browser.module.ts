import { Module } from '@nestjs/common';
import { BrowserService } from './browser.service';
import { PlaywrightService } from './playwright.service';

@Module({
  providers: [BrowserService, PlaywrightService],
  exports: [BrowserService],
})
export class BrowserModule {}
