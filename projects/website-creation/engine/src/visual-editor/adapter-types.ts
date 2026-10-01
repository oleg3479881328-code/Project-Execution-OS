import type { Config, Data } from "@puckeditor/core";

export type VisualEditorViewport = {
  label: string;
  width: number;
  height?: number;
};

export type VisualEditorProjectMeta = {
  projectId: string;
  pageId: string;
  pageLabel?: string;
  publicUrl?: string;
  viewports?: VisualEditorViewport[];
};

export type VisualEditorSaveResult = {
  ok: boolean;
  message?: string;
  version?: string;
};

export type VisualEditorAdapter = {
  config: Config;
  initialData: Data;
  meta: VisualEditorProjectMeta;
  saveDraft: (data: Data) => Promise<VisualEditorSaveResult>;
  publish?: (data: Data) => Promise<VisualEditorSaveResult>;
};
