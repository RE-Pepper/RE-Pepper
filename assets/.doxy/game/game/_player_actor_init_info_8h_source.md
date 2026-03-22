

# File PlayerActorInitInfo.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerActorInitInfo.h**](_player_actor_init_info_8h.md)

[Go to the documentation of this file](_player_actor_init_info_8h.md)


```C++
#pragma once

struct PlayerModelInfo
{
        const char** modelArcs;

        const char* getModelArchive( int index ) const
        {
                return modelArcs[ index ];
        }
};

struct PlayerAnimInfo
{
        const char** animArcs;

        const char* getAnimArchive( int index ) const
        {
                return animArcs[ index ];
        }
};

class PlayerActorInitInfo
{
        const PlayerModelInfo* mModelInfo;
        const PlayerAnimInfo*  mAnimInfo;
        void*                  _8;

public:
        PlayerActorInitInfo();
};
```


