import * as migration_20260914_171640_initial from './20260914_171640_initial';

export const migrations = [
  {
    up: migration_20260914_171640_initial.up,
    down: migration_20260914_171640_initial.down,
    name: '20260914_171640_initial'
  },
];
