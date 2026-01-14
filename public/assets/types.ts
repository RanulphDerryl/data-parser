interface DataParserConfig {
  /**
   * API endpoint URL
   */
  apiUrl: string;
  /**
   * Authorization token
   */
  authToken: string;
  /**
   * Data parser mode (e.g., CSV, JSON)
   */
  mode: 'csv' | 'json';
  /**
   * File path to save the parsed data
   */
  filePath: string;
  /**
   * Maximum number of rows to fetch at once
   */
  maxRows: number;
}

interface Data {
  id: number;
  createdAt: Date;
  updated_at: Date;
  title: string;
  description: string;
  type: string;
  link: string;
}

interface DataResponse {
  data: Data[];
  meta: {
    count: number;
    pages: number;
  };
}