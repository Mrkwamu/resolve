import { Injectable, Logger } from '@nestjs/common';
import { PlaywrightService } from './playwright.service';

@Injectable()
export class BrowserService {
  private readonly logger = new Logger(Logger.name);
  constructor(private readonly playwrightService: PlaywrightService) {}

  async openUrl(url: string): Promise<void> {
    const context = await this.playwrightService.createContext();
    try {
      const page = await context.newPage();
      await page.goto(url);
    } finally {
      this.logger.log('Closing context');
    }
  }
}
