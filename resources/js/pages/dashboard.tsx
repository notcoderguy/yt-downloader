import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Progress } from '@/components/ui/progress'
import { useState } from 'react'
import AppLayout from '@/layouts/app-layout'
import { Head } from '@inertiajs/react'
import { BreadcrumbItem } from '@/types'

type Download = {
  status: string;
  output?: {
    title: string;
    ext: string;
  };
}

const breadcrumbs: BreadcrumbItem[] = [
  { title: 'Dashboard', href: '/dashboard' },
]

export default function Dashboard() {
  const [url, setUrl] = useState('')
  const [downloads, setDownloads] = useState<Download[]>([])
  const [isDownloading, setIsDownloading] = useState(false)

  const handleDownload = async () => {
    setIsDownloading(true)
    try {
      const response = await fetch('/api/download', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || '',
          'X-Requested-With': 'XMLHttpRequest',
        },
        credentials: 'include',
        body: JSON.stringify({ url })
      })
      
      if (response.status === 401) {
        window.location.href = '/login'
        return
      }
      const data = await response.json()
      setDownloads([...downloads, data])
    } catch (error) {
      console.error('Download failed:', error)
    } finally {
      setIsDownloading(false)
      setUrl('')
    }
  }

  return (
    <AppLayout breadcrumbs={breadcrumbs}>
      <Head title="Dashboard" />
      <div className="space-y-6 px-4">
        <Card>
          <CardHeader>
            <CardTitle>Download Videos</CardTitle>
            <CardDescription>Enter YouTube URL to download</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex space-x-2">
              <Input
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://www.youtube.com/watch?v=..."
              />
              <Button onClick={handleDownload} disabled={isDownloading || !url}>
                {isDownloading ? 'Downloading...' : 'Download'}
              </Button>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Download Status</CardTitle>
            <CardDescription>Current and past downloads</CardDescription>
          </CardHeader>
          <CardContent>
            {downloads.length === 0 ? (
              <p className="text-muted-foreground">No downloads yet</p>
            ) : (
              <div className="space-y-4">
                {downloads.map((download, index) => (
                  <div key={index} className="border rounded-lg p-4">
                    <div className="flex justify-between mb-2">
                      <span>{download.output?.title || 'Unknown video'}</span>
                      <span className="text-green-500">Completed</span>
                    </div>
                    <Progress value={100} className="h-2" />
                  </div>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      </div>
    </AppLayout>
  )
}
