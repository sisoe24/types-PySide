import re
import pathlib


POST_GLOBAL_FIXES = [
    {
        'pattern': r'typing\.Callable',
        'sub': 'typing.Callable[..., Any]'
    },
    {
        'pattern': r'(?<!\.)ClassVar',
        'sub': 'typing.ClassVar'
    },
    {
        'pattern': r'(?<!\.)Any',
        'sub': 'typing.Any'
    },
]


def apply_post_global_fixes():
    """Applies the post global fixes to the .pyi files in the .build directory."""

    print('Applying post global fixes to .pyi files...')

    for file in pathlib.Path(__file__).parent.glob('.build/**/*.pyi'):

        with file.open('r+') as f:
            content = f.read()

            for fix in POST_GLOBAL_FIXES:
                content = re.sub(fix['pattern'], fix['sub'], content, flags=re.MULTILINE)

            f.seek(0)
            f.write(content)
            f.truncate()


if __name__ == '__main__':
    apply_post_global_fixes()
