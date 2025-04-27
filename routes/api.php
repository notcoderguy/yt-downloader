<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\VideoController;

Route::get('/health', function () {
    return response()->json([
        'status' => 'ok',
        'message' => 'API is running'
    ]);
});

// Route::middleware('auth:sanctum')->group(function () {
    // Route::get('/downloads', function () {
    //     return response()->json([
    //         'message' => 'Downloads endpoint'
    //     ]);
    // });
    Route::post('/download', [VideoController::class, 'download']);
// });
