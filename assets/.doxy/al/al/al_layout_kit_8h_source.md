

# File alLayoutKit.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Layout**](dir_df428175ad75013516ece83f85ae05d3.md) **>** [**alLayoutKit.h**](al_layout_kit_8h.md)

[Go to the documentation of this file](al_layout_kit_8h.md)


```C++
#pragma once

namespace al
{
class ExecuteDirector;
class FontHolder;

class LayoutKit
{
private:
        void*            _0;
        FontHolder*      mFontHolder;
        ExecuteDirector* mExecuteDirector;
        void*            _C;
        void*            _10;
        void*            _14;

public:
        void createExecuteDirector( int p );
        void createEffectSystem();
        void update();

public:
        LayoutKit( FontHolder* fontHolder );
};

} // namespace al
```


