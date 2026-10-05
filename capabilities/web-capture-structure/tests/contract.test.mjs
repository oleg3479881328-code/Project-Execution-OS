import test from 'node:test';
import assert from 'node:assert/strict';
import { captureStructureFromPage, SCHEMA } from '../src/index.mjs';

const strings = ['#document','HTML','BODY','DIV','#text','hello','https://example.test/','Example','display','block','position','static','id','hero'];
const fakeSnapshot = {
  strings,
  documents: [{
    documentURL: 6, title: 7, baseURL: 6, contentWidth: 1200, contentHeight: 1800, scrollOffsetX: 0, scrollOffsetY: 0,
    nodes: {
      parentIndex: [-1,0,1,2,3],
      nodeType: [9,1,1,1,3],
      nodeName: [0,1,2,3,4],
      nodeValue: [0,0,0,0,5],
      attributes: [[],[],[],[12,13],[]]
    },
    layout: {
      nodeIndex: [1,2,3,4],
      bounds: [[0,0,1200,1800],[0,0,1200,1800],[10,20,500,100],[10,20,100,20]],
      styles: [[9,11],[9,11],[9,11],[9,11]],
      paintOrders: [0,1,2,3]
    }
  }]
};

function fakePage() {
  const session = { send: async () => fakeSnapshot, detach: async () => {} };
  return {
    evaluate: async () => ({ url:'https://example.test/', title:'Example', viewport:{width:1200,height:800,devicePixelRatio:1}, scroll:{x:0,y:0}, document:{width:1200,height:1800} }),
    context: () => ({ newCDPSession: async () => session })
  };
}

test('returns stable normalized contract', async () => {
  const result = await captureStructureFromPage(fakePage(), { computedStyles:['display','position'] });
  assert.equal(result.schema, SCHEMA);
  assert.equal(result.block.id, 'web.capture_structure');
  assert.equal(result.provider, 'cdp-dom-snapshot');
  assert.equal(result.page.url, 'https://example.test/');
  assert.equal(result.documents.length, 1);
  assert.equal(result.documents[0].nodes.some(n => n.text === 'hello'), true);
  assert.equal(result.documents[0].nodes.find(n => n.tag === 'div').attrs.id, 'hero');
  assert.equal(result.styles.length, 1);
});
