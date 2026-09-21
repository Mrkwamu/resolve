import {
  Injectable,
  Logger,
  OnModuleDestroy,
  OnModuleInit,
} from '@nestjs/common';
import { Browser, BrowserContext, chromium } from 'playwright';
@Injectable()
export class PlaywrightService implements OnModuleInit, OnModuleDestroy {
  private readonly logger = new Logger(PlaywrightService.name);
  private browser!: Browser;

  async onModuleInit() {
    this.browser = await chromium.launch({
      headless: false,
      channel: 'chrome',
    });

    const isConnected = this.browser.isConnected();
    if (isConnected) {
      this.logger.log('Chromium is connected');
    } else {
      this.logger.error('Chromium is not connected');
    }
  }

  async createContext(): Promise<BrowserContext> {
    return this.browser.newContext();
  }

  async onModuleDestroy() {
    await this.browser.close();
  }
}
