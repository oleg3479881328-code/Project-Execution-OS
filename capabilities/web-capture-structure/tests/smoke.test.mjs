import test from 'node:test';
import assert from 'node:assert/strict';
import { captureStructureFromPage } from '../src/index.mjs';

test('auto provider falls back to DOM capture and returns usable structure', async () => {
  let calls = 0;
  const page = {
    context: () => ({ newCDPSession: async () => { throw new Error('unsupported bridge'); } }),
    evaluate: async (_fn, arg) => {
      calls += 1;
      if (calls === 1) return { url:'https://fallback.test/', title:'Fallback', viewport:{width:800,height:600,devicePixelRatio:1}, scroll:{x:0,y:0}, document:{width:800,height:1200} };
      assert.ok(Array.isArray(arg.styleProperties));
      return { nodes:[{id:'d0:n0',kind:'document',visible:true},{id:'d0:n1',parent:'d0:n0',kind:'element',tag:'body',bounds:[0,0,800,1200],styleRef:0,visible:true}], styles:[['block']] };
    }
  };
  const result = await captureStructureFromPage(page, { computedStyles:['display'] });
  assert.equal(result.provider, 'dom-evaluate-fallback');
  assert.equal(result.stats.nodes, 2);
  assert.match(result.warnings[0], /fallback/i);
});
