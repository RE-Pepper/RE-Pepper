

# File GhostPlayerRecorder.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**GhostPlayerRecorder.cpp**](_ghost_player_recorder_8cpp.md)

[Go to the documentation of this file](_ghost_player_recorder_8cpp.md)


```C++
#include "Player/GhostPlayerRecorder.h"

GhostPlayerRecorder::GhostPlayerRecorder()
    : mFrames( nullptr ), mGhostPlayer( nullptr ), mNumFrames( 0 ), mCurrentFrame( 0 ), _14( 0 ), _18( 0 ),
      _1C( true ), _1D( true )
{
}

void GhostPlayerRecorder::create( int numFrames )
{
        if ( mFrames )
                delete[] mFrames;
        mFrames       = new Frame[ numFrames ];
        mCurrentFrame = 0;
        _1C           = 1;
        mNumFrames    = numFrames;
}

#ifdef NON_MATCHING
void GhostPlayerRecorder::initSceneObj()
{
}
#endif
```


