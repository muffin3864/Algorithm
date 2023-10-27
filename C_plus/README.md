#### 환경설정 
VS Code에서 C/C++ 코딩환경 구축하기

https://velog.io/@youhyeoneee/%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95-VS-Code-%EC%97%90%EC%84%9C-CC-%EC%BD%94%EB%94%A9-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-Windows

# 기본 지식

## 텍스트 파일 읽어와서 실행

```cpp
std::ifstream readFile;         //읽을 목적의 파일 선언
readFile.open("words.txt");     //파일 열기
if(readFile.is_open())          //파일이 열렸는지 확인
{
    while(!readFile.eof())      //파일 끝까지 읽었는지 확인
    {
        char arr[256];
        readFromFile.getline(arr, 256); //한줄씩 읽어오기
    }
}
readFile.close();               //파일 닫기
```

