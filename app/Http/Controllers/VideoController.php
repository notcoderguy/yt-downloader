<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class VideoController extends Controller
{
    public function download(Request $request)
    {
        $request->validate([
            'url' => 'required|url',
            'format' => 'sometimes|string',
            'quality' => 'sometimes|string',
        ]);

        try {
            $response = Http::post(env('FASTAPI_URL').'/download', [
                'url' => $request->url,
                'format' => $request->format ?? 'mp4',
                'quality' => $request->quality ?? 'best',
            ]);

            if ($response->failed()) {
                Log::error('FastAPI download failed', [
                    'status' => $response->status(),
                    'error' => $response->body(),
                ]);

                return response()->json([
                    'error' => 'Download failed',
                    'details' => $response->json(),
                ], $response->status());
            }

            return $response->json();

        } catch (\Exception $e) {
            Log::error('FastAPI connection error', [
                'error' => $e->getMessage(),
            ]);

            return response()->json([
                'error' => 'Service unavailable',
                'details' => $e->getMessage(),
            ], 503);
        }
    }
}
