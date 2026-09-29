import config from '@payload-config'
import {
  REST_DELETE,
  REST_GET,
  REST_OPTIONS,
  REST_PATCH,
  REST_POST,
  REST_PUT,
} from '@payloadcms/next/routes'

const disabledForCsg = () => process.env.CSG_GITHUB_MODE !== '0'
const csgResponse = () => Response.json({ ok: false, error: 'Payload API is disabled for the Git-backed Car Service Garage runtime.' }, { status: 404 })

export const GET = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_GET(config)(request, context as any)
export const POST = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_POST(config)(request, context as any)
export const DELETE = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_DELETE(config)(request, context as any)
export const PATCH = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_PATCH(config)(request, context as any)
export const PUT = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_PUT(config)(request, context as any)
export const OPTIONS = async (request: Request, context: unknown) => disabledForCsg() ? csgResponse() : REST_OPTIONS(config)(request, context as any)
