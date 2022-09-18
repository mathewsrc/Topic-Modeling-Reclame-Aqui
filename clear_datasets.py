import click
import os

def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()
        

@click.command()
@click.option('--yes', is_flag=True, callback=abort_if_false, expose_value=False,
                prompt='Are you sure you want to delete file ?')
def deleteDatasetFiles():
    try:
        filename = 'web_scraping_results.csv'
        location = './results/'
        path = os.path.join(location, filename)
        if(os.path.exists(path)):
            os.remove(path)
            click.echo('Deleted all files!')
        else:
            click.echo('File does not exist in this directory!')
    except:
        click.echo('Error to delete files!')
    
    
if __name__=='__main__':
    deleteDatasetFiles()
