<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Support\Facades\File;

class CreateStorageLinks extends Command
{
    protected $signature = 'storage:links:custom';
    protected $description = 'Create custom storage links for downloads';

    public function handle()
    {
        // Link api downloads to storage
        $target = storage_path('app/private/downloads');
        $link = base_path('api/downloads');

        if (!file_exists($target)) {
            File::makeDirectory($target, 0755, true);
        }

        if (file_exists($link)) {
            $this->error("The link [$link] already exists.");
            return;
        }

        symlink($target, $link);
        $this->info("The [$link] link has been connected to [$target].");
    }
}
