import { Body, Controller, Post } from '@nestjs/common';
import { BrowserService } from './browser/browser.service';

@Controller('playwright')
export class AppController {
  constructor(private readonly browserService: BrowserService) {}

  @Post('url') async openBrowser(@Body('url') url: string) {
    await this.browserService.openUrl(url);
    return { message: 'Browser opened' };
  }
}
