

# File PlayerInitFunc.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerInitFunc.h**](_player_init_func_8h.md)

[Go to the documentation of this file](_player_init_func_8h.md)


```C++
#pragma once

struct PlayerModelInfo;
struct PlayerAnimInfo;

namespace PlayerInitFunc
{

const PlayerModelInfo* getModelInfo();
const PlayerAnimInfo*  getAnimInfo();
void*                  fn_00260620();

} // namespace PlayerInitFunc
```


